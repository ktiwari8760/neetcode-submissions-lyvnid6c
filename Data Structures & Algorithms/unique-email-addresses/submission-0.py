class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # emails = [mail.replace("." , "") for mail in emails]
        print(emails)
        emails = [(mail.split("@")[0] , mail.split("@")[1]) for mail in emails]
        emails = [(local.split("+")[0].replace("." , "") , domain) for local , domain in emails]
        emails = set(emails)
        return len(emails)