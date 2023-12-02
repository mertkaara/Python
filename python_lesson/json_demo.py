import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        
        # load users from .json file
        self.loadUsers()    # loadUsers burada çağırıldığı için başlangıçta kullanıcı bilgilerini yazdırır
    
    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json','r',encoding='utf-8') as file:
                users = json.load(file)     # Bunlar şu and json string formatında bu şekilde içinden bir obje çağıramayız
                print(users)
                for user in users:
                    user = json.loads(user) # json sting formatında olan user bilgisini dict formatına çeviriyoruz
                    newUser = User(username= user['username'], password= user['password'], email= user['email'])
                    self.users.append(newUser)
            print(self.users)
                
    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print('Kullanıcı oluşturuldu.')
    
    def login(self, username, password):
        for user in self.users:
                if user.username == username and user.password == password:
                    self.isLoggedIn = True
                    self.currentUser = user
                    print('\nLogin yapıldı.\n')
                    break
        
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('\nÇıkış Yapıldı\n')
    
    def identity(self):
        if self.isLoggedIn:
            print(f'\nusername:{self.currentUser.username}\n')
        else:
            print('\nGiriş yapılmadı.\n')
    
    def savetoFile(self):
        myList = []
        
        for user in self.users:
            myList.append(json.dumps(user.__dict__))
        
        with open('users.json','w') as file:
            json.dump(myList, file)

repository = UserRepository()
    
while True:
    print("Menü".center(50,'*'))
    secim = input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçiminiz:")
    if secim == '5':
        break
    else: 
        if secim == '1':
            username = input ('username:')
            passord = input ('password:')
            email = input ('email:')
            
            user = User(username=username, password=passord, email=email)
            repository.register(user)
            print(repository.users)
            
        elif secim == '2':
            #login
            if repository.isLoggedIn:
                print('\nZaten giriş yapılmış.\n')
            else:
                username = input('username:')
                password = input('password:')
                repository.login(username, password)
                
        elif secim == '3':
            #logout
            repository.logout()
        
        elif secim == '4':
            #display username
            repository.identity()
        
        else:
            print("Yanlış seçim.")