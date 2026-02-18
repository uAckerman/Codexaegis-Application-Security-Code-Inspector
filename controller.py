from sql_injection import SQLInjectionCheck

class InspectionController:
    def __init__(self, base_url):
        self.base_url = base_url
        self.checks = []

    def register_check(self, check):
        self.checks.append(check)

    def run(self):
        results = []
        for check in self.checks:
            result = check.run(self.base_url)
            results.append(result)
        return results
