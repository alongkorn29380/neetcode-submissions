class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.i = 0
        self.l = 1

    def visit(self, url: str) -> None:
        self.i += 1
        if self.i == len(self.history):
            self.history.append(url)
            self.l += 1
        else:
            self.history[self.i] = url
            self.l = self.i + 1
    def back(self, steps: int) -> str:
        self.i = max(self.i - steps, 0)
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, self.l - 1)
        return self.history[self.i]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)