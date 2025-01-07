
"""
Event Modules Parser
"""

class EventParser:
    def __init__(self, events: list[dict] | tuple[dict]):
        self.events = events
        self.report: str = "\n".join(self.parse())

    def parse(self):
        """ report each event with it assosciate format """
        report = []
        for event in self.events:
            repo_name = event['repo']['name']
            event_type = event['type']
            payload = event.get('payload', {})

            if event_type == "CommitCommentEvent":
                action = payload.get('action', 'commented')
                comment = payload.get('comment', {}).get('id', 'a comment')
                report.append(f"- {action.capitalize()} on commit {comment} in {repo_name}")

            elif event_type == "CreateEvent":
                ref_type = payload.get('ref_type', "repository")
                ref = payload.get('ref', '')
                if ref:
                    report.append(f"- Created {ref_type} '{ref}' in {repo_name}")
                else:
                    report.append(f"- Created {ref_type} in {repo_name}")

            elif event_type == "DeleteEvent":
                ref_type = payload.get('ref_type', "repository")
                ref = payload.get('ref', '')
                if ref:
                    report.append(f"- Deleted {ref_type} '{ref}' in {repo_name}")
                else:
                    report.append(f"- Deleted {ref_type} in {repo_name}")

            elif event_type == "ForkEvent":
                forkee = payload.get('forkee', {}).get('full_name', "unknown repository")
                report.append(f"- Forked {repo_name} to {forkee}")

            elif event_type == "GollumEvent":
                pages = payload.get('pages', [])
                for page in pages:
                    action = page.get('action')
                    title = page.get('title')
                    report.append(f"- {action.capitalize()} wiki page '{title}' in {repo_name}")

            elif event_type == "IssuesEvent":
                action = payload.get('action')
                issue_number = payload.get('issue', {}).get('number')
                if action:
                    report.append(f"- {action.capitalize()} issue #{issue_number} in {repo_name}")
            
            elif event_type == "IssueCommentEvent":
                action = payload.get('action')
                issue_number = payload.get('issue', {}).get('number')
                if action:
                    report.append(f"- {action.capitalize()} a comment on issue #{issue_number} in {repo_name}")
            
            elif event_type == "MemberEvent":
                action = payload.get('action')
                member = payload.get('member', {}).get('login', 'a member')
                report.append(f"- {action.capitalize()} {member} in {repo_name}")

            elif event_type == "PublicEvent":
                report.append(f"- Made {repo_name} public")

            elif event_type == "PullRequestEvent":
                action = payload.get('action')
                pr_number = payload.get('pull_request', {}).get('number')
                if action:
                    report.append(f"- {action.capitalize()} pull request #{pr_number} in {repo_name}")
            
            elif event_type == "PullRequestReviewEvent":
                action = payload.get('action')
                pr_number = payload.get('pull_request', {}).get('number')
                if action:
                    report.append(f"- {action.capitalize()} a review on pull request #{pr_number} in {repo_name}")
            
            elif event_type == "PullRequestReviewCommentEvent":
                action = payload.get('action')
                pr_number = payload.get('pull_request', {}).get('number')
                if action:
                    report.append(f"- {action.capitalize()} a review comment on pull request #{pr_number} in {repo_name}")

            elif event_type == "PullRequestReviewThreadEvent":
                action = payload.get('action', "performed an action")
                report.append(f"- {action.capitalize()} on a pull request review thread in {repo_name}")

            elif event_type == "PushEvent":
                commits = len(payload.get('commits', []))
                report.append(f"- Pushed {commits} commits to {repo_name}")

            elif event_type == "ReleaseEvent":
                action = payload.get('action')
                release_tag = payload.get('release', {}).get('tag_name', 'a release')
                report.append(f"- {action.capitalize()} {release_tag} in {repo_name}")

            elif event_type == "SponsorshipEvent":
                action = payload.get('action', 'performed sponsorship action')
                sponsor = payload.get('sponsorship', {}).get('sponsor', {}).get('login', 'a sponsor')
                report.append(f"- {action.capitalize()} with {sponsor}")

            elif event_type == "WatchEvent":
                action = payload.get('action')
                if action == "started":
                    report.append(f"- Starred {repo_name}")

        return report
