from fastapi import Request
from utils.logger import Logger
from datetime import datetime

logger = Logger()

async def log_requests(request: Request, call_next):
    """Log all API requests"""
    start_time = datetime.utcnow()
    
    # Log request details
    logger.log_activity(
        user_id="system",
        action="API_REQUEST",
        details={
            "method": request.method,
            "url": str(request.url),
            "client_ip": request.client.host,
            "timestamp": start_time.isoformat()
        }
    )
    
    response = await call_next(request)
    
    # Log response details
    end_time = datetime.utcnow()
    duration = (end_time - start_time).total_seconds()
    
    logger.log_activity(
        user_id="system",
        action="API_RESPONSE",
        details={
            "status_code": response.status_code,
            "duration": duration,
            "timestamp": end_time.isoformat()
        }
    )
    
    return response
