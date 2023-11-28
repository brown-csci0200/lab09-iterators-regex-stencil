import re

class Registrar:
    def __init__(self, file):
        """
        :param file: the path to the file that you should read in
        """
        self.document = read_to_string(file)
        self.email_regex = r"" # TODO: determine what regex will match on emails
        self.course_regex = r"" # TODO: determine what regex will match on course codes 

    def view_emails(self):
        """
        :return: all of the emails in the document
        """
        # TODO: find all of the email matches in self.document
        matches = []
        return matches

    def view_courses(self):
        """
        :return: all of the courses in the document
        """
        # TODO: find all of the course code matches in self.document!
        matches = []
        return matches

    def make_changes(self, to_change, replacement):
        """
        :param to_change: the subsequence of self.document that should be changed
        :param replacement: the string that will replace the matched regex
        :return: None; sets the document to the change that gets made
        """
        # TODO: write this method!
        pass

def read_to_string(filename):
    with open(filename, "r") as f:
        return f.read()

if __name__ == "__main__":
    registrar = Registrar("registrations.txt")

    # Try running your code with our provided text file and see if your results
    # look reasonable!
    print(registrar.view_emails())
    print(registrar.view_courses())

    registrar.make_changes(registrar.email_regex, "###")
    print(registrar.view_emails())

    # Feel free to write your own tests as well!
