def validate_date(date_str):
    from datetime import datetime
    try :
        datetime.strptime(date_str , "%Y-%m-%d")
    except ValueError :
        raise ValueError("Date must be in YYYY-MM-DD format")
    