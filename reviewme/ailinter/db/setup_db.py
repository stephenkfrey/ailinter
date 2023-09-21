import sys
sys.path.insert(0, './local_db')

from local_db.db_functions import create_db, load_db, write_issue, read_issues

create_db('test_db')

session = load_db('test_db')

write_issue(session, 'deva', 'query', 'response', 'conversation_history', 'prompt', 'retrievals')
issues = read_issues(session)
for issue in issues:
    print ('next issue--')
    print(issue.id, issue.timestamp, issue.deva_username, issue.query, issue.response, issue.conversation_history, issue.prompt, issue.retrievals)