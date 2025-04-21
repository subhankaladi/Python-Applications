class CareerAdvice:
    def __init__(self, interest):
        self.interest = interest

    def get_advice(self):
        if "coding" in self.interest:
            return "Software Engineer, AI Developer"
        elif "design" in self.interest:
            return "UI/UX Designer, Graphic Artist"
        elif "business" in self.interest:
            return "Entrepreneur, Business Analyst"
        else:
            return "Try exploring new fields with online courses."
