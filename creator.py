import os, binascii, httpx, random, string, threading, json
from lib.console import Console
from lib.utils import Util
config = json.load(open('./input/config.json', 'r+'))
class AccCreator(threading.Thread):
    def __init__(self, proxy):
        self.api: Util = Util(proxy)
        self.proxy: str = proxy 
        self.baseurl: str = 'https://www.guilded.gg/api'
        self.username: str = f'xKian-{str(binascii.b2a_hex(os.urandom(8)).decode("utf-8"))}'
        self.password: str  = "".join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10)])
        self.email: str = f'{str(binascii.b2a_hex(os.urandom(10)).decode("utf-8"))}@gmail.com'
        names = ['Olivia', 'Emma', 'Charlotte', 'Amelia', 'Ava', 'Sophia', 'Isabella', 'Mia', 'Evelyn', 'Harper', 'Luna', 'Camila', 'Gianna', 'Elizabeth', 'Eleanor', 'Ella', 'Abigail', 'Sofia', 'Avery', 'Scarlett', 'Emily', 'Aria', 'Penelope', 'Chloe', 'Layla', 'Mila', 'Nora', 'Hazel', 'Madison', 'Ellie', 'Lily', 'Nova', 'Isla', 'Grace', 'Violet', 'Aurora', 'Riley', 'Zoey', 'Willow', 'Emilia', 'Stella', 'Zoe', 'Victoria', 'Hannah', 'Addison', 'Leah', 'Lucy', 'Eliana', 'Ivy', 'Everly', 'Lillian', 'Paisley', 'Elena', 'Naomi', 'Maya', 'Natalie', 'Kinsley', 'Delilah', 'Claire', 'Audrey', 'Aaliyah', 'Ruby', 'Brooklyn', 'Alice', 'Aubrey', 'Autumn', 'Leilani', 'Savannah', 'Valentina', 'Kennedy', 'Madelyn', 'Josephine', 'Bella', 'Skylar', 'Genesis', 'Sophie', 'Hailey', 'Sadie', 'Natalia', 'Quinn', 'Caroline', 'Allison', 'Gabriella', 'Anna', 'Serenity', 'Nevaeh', 'Cora', 'Ariana', 'Emery', 'Lydia', 'Jade', 'Sarah', 'Eva', 'Adeline', 'Madeline', 'Piper', 'Rylee', 'Athena', 'Peyton', 'Everleigh', 'Liam', 'Noah', 'Oliver', 'Elijah', 'James', 'William', 'Benjamin', 'Lucas', 'Henry', 'Theodore', 'Jack', 'Levi', 'Alexander', 'Jackson', 'Mateo', 'Daniel', 'Michael', 'Mason', 'Sebastian', 'Ethan', 'Logan', 'Owen', 'Samuel', 'Jacob', 'Asher', 'Aiden', 'John', 'Joseph', 'Wyatt', 'David', 'Leo', 'Luke', 'Julian', 'Hudson', 'Grayson', 'Matthew', 'Ezra', 'Gabriel', 'Carter', 'Isaac', 'Jayden', 'Luca', 'Anthony', 'Dylan', 'Lincoln', 'Thomas', 'Maverick', 'Elias', 'Josiah', 'Charles', 'Caleb', 'Christopher', 'Ezekiel', 'Miles', 'Jaxon', 'Isaiah', 'Andrew', 'Joshua', 'Nathan', 'Nolan', 'Adrian', 'Cameron', 'Santiago', 'Eli', 'Aaron', 'Ryan', 'Angel', 'Cooper', 'Waylon', 'Easton', 'Kai', 'Christian', 'Landon', 'Colton', 'Roman', 'Axel', 'Brooks', 'Jonathan', 'Robert', 'Jameson', 'Ian', 'Everett', 'Greyson', 'Wesley', 'Jeremiah', 'Hunter', 'Leonardo', 'Jordan', 'Jose', 'Bennett', 'Silas', 'Nicholas', 'Parker', 'Beau', 'Weston', 'Austin', 'Connor', 'Carson', 'Dominic', 'Xavier', 'Kai', 'Zion', 'Jayden', 'Eliana', 'Luca', 'Ezra', 'Maeve', 'Aaliyah', 'Mia', 'Nova', 'Aurora', 'Amara', 'Kayden', 'Ivy', 'Alina', 'Mila', 'Quinn', 'Rowan', 'Elliot', 'Finn', 'Lilibet', 'River', 'Xavier', 'Rachel', 'Amaya', 'Remi', 'Axel', 'Zoey', 'Malachi', 'Alex', 'Blake', 'Lyla', 'Alice', 'Isla', 'Rebecca', 'Rohan', 'Milo', 'Elias', 'Ari', 'Aria', 'Molly', 'Jude', 'Isabella', 'Arthur', 'Millie', 'Andrea', 'Marcus', 'Atlas', 'Ariella', 'Kyle', 'Evan', 'Ira', 'Hayden', 'Bailey', 'Gianna', 'Valerie', 'Brianna', 'Jesse', 'Cecilia', 'Leo', 'Leilani', 'Dante', 'Zoe', 'Khadijah', 'Mya', 'Sharon', 'Sean', 'Brielle', 'Ayla', 'Shia', 'Riley', 'Raya', 'Sloane', 'Alana', 'Charlie', 'Kian', 'Hudson', 'Elise', 'Akira', 'Mika', 'Freya', 'Nia', 'Natasha', 'Myra', 'Mateo', 'Everett', 'Rae', 'Savannah', 'Thea', 'Finley', 'Alaina', 'Mina', 'Yara', 'Emerson', 'Camille', 'Ivan', 'Skyler', 'Skylar', 'Alma', 'Reese', 'Sasha', 'Asa', 'Sage', 'Camila', 'Amira', 'Kieran', 'Monica', 'Everly', 'Evie', 'Maverick', 'Kyra', 'Ian', 'Julia', 'Vivian', 'Theo', 'Ophelia', 'Chelsea', 'Azariah', 'Jade', 'Lara', 'Ava', 'Morgan', 'Lennox', 'Luna', 'Isabelle', 'Amir', 'Rhys', 'Arlo', 'Giovanni', 'Aisha', 'Orion', 'Ahmed', 'Nolan', 'Ezekiel', 'Michelle', 'Lea', 'Silas', 'Elaine', 'Adira', 'Callan', 'Lilith', 'Justin', 'Simon', 'Rhea', 'Marie', 'Lisa', 'Damien', 'Ximena', 'Lilah', 'Elora', 'Sienna', 'Fiona', 'Urban', 'Jean', 'Eden', 'Kayla', 'Avi', 'Octavia', 'Skye', 'Nancy', 'Otis', 'Lila', 'Anya', 'Elena', 'Zayne', 'Gigi', 'Alyssa', 'Amelia', 'Giselle', 'Francis', 'Jacqueline', 'Aiden', 'Kylie', 'Wren', 'Maria', 'Mae', 'Colette', 'Louise', 'Aliyah', 'Chase', 'Tara', 'Lorenzo', 'Sydney', 'Callie', 'Niko', 'Avery', 'Gemma', 'Rafael', 'Hailey', 'Harlow', 'Adeline', 'Margot', 'Rory', 'Nyla', 'Helena', 'Colin', 'Xander', 'Rylee', 'Irene', 'Ashton', 'Marley', 'Arden', 'Kaira', 'Arianna', 'Pia', 'Nola', 'Miles', 'Brooks', 'Annalise', 'Imani', 'Josie', 'Ellis', 'Cali', 'Hadassah', 'Phoenix', 'Piper', 'Emery', 'Aliza', 'Mackenzie', 'Timothy', 'Adrian', 'Sawyer', 'Harvey', 'Enoch', 'Lachlan', 'Kaiden', 'Zuri', 'Shelby', 'Liam', 'Olivia', 'Aubrey', 'Sanjana', 'Rayne', 'Stella', 'Cleo', 'Gracie', 'Oakley', 'Madeline', 'Melissa', 'Lauren', 'Mona', 'Alicia', 'Jasmine', 'Scott', 'Abel', 'Elliott', 'Wesley', 'Aditya', 'Alan', 'Brooke', 'Sunny', 'Sana', 'Blair', 'Leon', 'Emmanuel', 'Lilian', 'Priya', 'Malia', 'Elodie', 'Adriel', 'Amos', 'Trisha', 'Naomi', 'Damian', 'Nevaeh', 'Judah', 'Sloan', 'Joel', 'Nicholas', 'Azriel', 'Lyra', 'Lee', 'Kevin', 'Remy', 'Omar', 'Amelie', 'Caleb', 'Aleena', 'Killian', 'Theodore', 'Asher', 'Mariam', 'Claudia', 'Noelle', 'Juliana', 'Makayla', 'Beau', 'Nikita', 'Beckett', 'Nadia', 'Ana', 'Zane', 'Jayce', 'Brayden', 'Elia', 'Leia', 'Cooper', 'Zain', 'Ronan', 'Liana', 'Kali', 'Serena', 'Davina', 'Zaid', 'Dillon', 'Sylvia', 'Rhiannon', 'Ryder', 'Zara', 'Amina', 'Keanu', 'Amaris', 'Eloise', 'Mara', 'Vera', 'Sonny', 'Keira', 'Ali', 'Sierra', 'Harper', 'Katherine', 'Siobhan', 'Ada', 'Gia', 'Heather', 'Kalani', 'Penny', 'Camilla', 'Cole', 'Amani', 'Emmet', 'Leila', 'Ethan', 'Alani', 'Fallon', 'Joyce', 'Joan', 'Winifred', 'Amyra', 'Mira', 'Quincy', 'Kimberly', 'Faye', 'Colton', 'Cayden', 'Maira', 'Ayana', 'Shiloh', 'Darren', 'Evelyn', 'Lorelei', 'Iva', 'Felix', 'Tessa', 'Jalen', 'Rylan', 'Nellie', 'Masha', 'Amora', 'Alvin', 'Leighton', 'Keziah', 'Mikayla', 'Harley', 'Oliver', 'Huxley', 'Martin', 'Noa', 'Rocco', 'Shane', 'Ines', 'Rai', 'Harry', 'Lily', 'Stanley', 'Darcy', 'Bryce', 'Devin', 'Lucas', 'Jamie', 'Teddy', 'Martha', 'Albert', 'Travis', 'Lucian', 'Emelia', 'Delilah', 'Norah', 'Azalea', 'Valentina', 'Hallie', 'Nora', 'Kara', 'Misha', 'Ishmael', 'Mimi', 'Pamela', 'Genevieve', 'Thalia', 'Collin', 'Grayson', 'June', 'May', 'Kenji', 'Chiara', 'Ravi', 'Rosie', 'Seraphina', 'Juno', 'Sophie', 'Simone', 'Gavin', 'Alayna', 'Miriam', 'Patricia', 'Christine', 'Joaquin', 'Dior', 'Israel', 'Teagan', 'Jocelyn', 'Zaira', 'Tiffany', 'Cedric', 'Reyna', 'Winston', 'Maximus', 'Dennis', 'George', 'Braxton', 'Deborah', 'Lorraine', 'Romy', 'Dakota', 'Reuben', 'Hayley', 'Anisha', 'Saira', 'Veda', 'Tiana', 'Kyler', 'Preston', 'Olive', 'Ellie', 'Rio', 'Yvonne', 'Parker', 'Yana', 'Maia', 'Levi', 'Tyson', 'Graham', 'Cain', 'Kelvin', 'Lynn', 'Lia', 'Kaden', 'Rian', 'Aurelia', 'Spencer', 'Usnavi', 'Elina', 'Ellen', 'Kaya', 'Tamara', 'Mabel', 'Remington', 'Ember', 'Sadie', 'Sahil', 'Azrael', 'Kendall', 'Raine', 'Noah', 'Athena', 'Declan', 'Leigh', 'Helen', 'Rey', 'Janet', 'Ace', 'Alena', 'Lola', 'Karina', 'Grace', 'Jedidiah', 'Alaia', 'Aman', 'Brian', 'Milan', 'Malcolm', 'Javier', 'Emma', 'Marion', 'Adaline', 'Daisy', 'Amal', 'Holly', 'Cillian', 'Kayleigh']
        self.fullname: str = random.choice(names)
    @staticmethod
    def randomstring(lenght: int) -> str:
        return str(binascii.b2a_hex(os.urandom(lenght)).decode('utf-8'))
    def start(self):
        payload: dict = {"extraInfo":{"platform":"desktop"},"name":self.username,"email":self.email,"password":self.password,"fullName":self.fullname}
        headers: dict = {
            'authority': 'www.guilded.gg',
            'method': 'POST',
            'path': '/api/users?type=email',
            'scheme': 'https',

            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'fr-FR,fr;q=0.9',
            'content-type': 'application/json',
            'guilded-client-id': f'{self.randomstring(8)}-{self.randomstring(4)}-{self.randomstring(4)}-{self.randomstring(4)}-{self.randomstring(12)}',
            'guilded-device-id': self.randomstring(64),
            'guilded-device-type': 'desktop',
            'guilded-stag': self.randomstring(32),
            'origin': 'https://www.guilded.gg',
            'referer': 'https://www.guilded.gg/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'dnt': '1',
            "Sec-Ch-Ua": '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            "Sec-Ch-Ua-Mobile": '?0',
            "Sec-Ch-Ua-Platform": "macOS",
        }
        try:
            if config["proxy"]:proxies = f'http://{self.proxy}' 
            else: proxies = None
            with httpx.Client(proxies=None, headers=headers) as client:
                r = client.post(f'{self.baseurl}/users?type=email', json=payload)
                if "banned" in r.text:
                    Console.printl("[>] Banned")
                    return
                if "email" not in r.text:
                    Console.debug("[*] Rate limited")
                    return
                worked, cookie = self.api.login(self.email, self.password)
                if worked:
                    Console.printl(f"[+] Created {self.username}")
                    with open("./output/accounts.txt", "a+") as f:
                        f.write(f"{self.email}:{self.password}:{cookie['hmac_signed_session']}\n")
                    with open("./output/cookies.txt", "a+") as f:
                        f.write(f"{cookie['hmac_signed_session']}\n")
                else:
                    Console.printl(f"[-] Failed to create {self.username}")
                    
        except Exception as e:
            Console.debug(f'[*]: {e}')