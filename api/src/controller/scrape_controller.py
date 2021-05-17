from service.scrape_service import scrape_logic_by_id

def scrape_by_id(account_id, limit):
    return scrape_logic_by_id(account_id, limit)

def scrape_honda(limit):
    return scrape_logic_by_id('keisuke_honda', limit)