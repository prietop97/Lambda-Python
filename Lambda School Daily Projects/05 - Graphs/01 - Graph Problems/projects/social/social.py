import random
from util import Queue
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
    def get_friends(self,user_id):
        return self.friendships[user_id]

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        possible_friendships = []

        for i in range(0, num_users):
            self.add_user(f"User {i}")
     
        total = 0
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                total+= 1
                possible_friendships.append((user_id, friend_id))
        print(total)
        # for user_id in self.users:
        #     skipping = num_users // avg_friendships
        #     for friend_id in range(user_id + 1, len(self.users) + 1, skipping):
        #         if total >= num_users * avg_friendships // 2:
        #             print(total)
        #             return

        #         self.add_friendship(user_id, friend_id)
        #         total += 1

        print(total)
        random.shuffle(possible_friendships)

        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        # Create friendships

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        q.enqueue([user_id])

        while q.size() > 0:
            path = q.dequeue()
            if path[-1] not in visited:
                visited[path[-1]] = path

                for friend in self.get_friends(path[-1]):
                    q.enqueue(path + [friend])

        return visited
    
    def get_percentages(self,user,cache):
        return f'User {user}: {cache[user] // len(self.users) * 100}%'



if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 5)
    #print(sg.friendships)
    connections = sg.get_all_social_paths(2)

    counter = 0
    for key,value in connections.items():
        if len(value) != 1:
            counter += 1

    print(f'{counter / len(sg.users) * 100}%')

    


# 10 
# 1                2              3         4           5          6           7           8          9         10
# 3 5 7 9         4 6 8 10       1 5 7 9    2 6 8 10    1 3 7 9    2 4 8 10    1 3 5 9     2 4 6 10   1 3 5 7   2 4 6 8