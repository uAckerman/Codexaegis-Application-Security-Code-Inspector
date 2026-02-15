class BaseCheck:
    name = "Base Check"

    def run(self, base_url):
        raise NotImplementedError("Each module must implement run()")
