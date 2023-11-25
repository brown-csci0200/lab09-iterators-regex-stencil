import re


def fill_in_doc(filename):
    f = open(filename, "r")
    string = f.readline()

    doc = ""
    while string:
        doc += string
        string = f.readline()

    return doc


class Registrar:
    def __init__(self, file):
        """
        :param file: the path to the file that you should read in
        """
        self.document = fill_in_doc(file)
        self.email_regex = r""  # TODO: determine what regex will match on emails
        self.course_regex = r""  # TODO: determine what regex will match on course codes

    def view_emails(self):
        """
        Prints all of the matches with the email regex
        :return: None; prints results
        """
        # TODO: find all of the email matches in self.document
        pass

    def view_courses(self):
        """
        prints all of the matches with the course regex
        :return: None; prints results
        """
        # TODO: find all of the course code matches in self.document!
        pass

    def make_changes(self, to_change, replacement):
        """
        :param to_change: the subsequence of self.document that should be changed
        :param replacement: the string that will replace the matched regex
        :return: None; sets the document to the change that gets made
        """
        # TODO: write this method!
        pass


if __name__ == "__main__":
    registrar = Registrar("registrations.txt")

    # Try running your code with our provided text file and see if your results
    # look reasonable!
    registrar.view_emails()
    registrar.view_courses()

    registrar.make_changes(registrar.email_regex, "###")
    registrar.view_emails()

    # Feel free to write your own tests as well!
