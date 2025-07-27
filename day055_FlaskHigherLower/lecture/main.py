class User:
    def __init__(self, name):
        self.name = name
        self.logged_in = False

    def user_auth(function):
        def wrapper(*args, **kwargs):
            if args[0].logged_in == True:
                function(args[0])

        return wrapper

    @user_auth
    def create_new_blog(self):
        print(f"This is {self.name}'s new blog.")


new_user = User("JIN")
new_user.logged_in = True
new_user.create_new_blog()
