import copy
from abc import ABC, abstractmethod


# Prototype Interface
class Document(ABC):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def display(self):
        pass


# Concrete Prototype: Resume
class Resume(Document):
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    def clone(self):
        return copy.deepcopy(self)

    def display(self):
        print(f"Resume of {self.name} with {self.experience} years of experience")


# Concrete Prototype: Report
class Report(Document):
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def clone(self):
        return copy.deepcopy(self)

    def display(self):
        print(f"Report titled '{self.title}' with content: {self.content}")


# Client code
def client():
    # Create prototype documents
    resume_template = Resume("John Doe", 5)
    report_template = Report("Q1 Summary", "Sales increased by 20%.")

    # Clone the prototypes
    resume_copy = resume_template.clone()
    resume_copy.name = "Jane Smith"
    resume_copy.experience = 3

    report_copy = report_template.clone()
    report_copy.title = "Q2 Summary"
    report_copy.content = "Sales increased by 30%."

    # Display cloned documents
    resume_template.display()
    resume_copy.display()
    report_template.display()
    report_copy.display()


# Run the client code
if __name__ == "__main__":
    client()
