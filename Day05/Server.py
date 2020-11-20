'''服务器'''
import asynchat
import asyncore

PORT = 8888

#创建异常抛出类
class EndSession(Exception):
    pass

class ChatServer(asyncore.dispatcher):
    '''创建服务器'''
    def __init__(self,port):
        asyncore.dispatcher.__init__(self)

        #创建socket
        self.create_socket()
        #设置socket可重用
        self.set_reuse_addr()
        #监听端口 绑定
        self.bind(('',port))
        #设置多用户登录
        self.listen(5)
        self.users = {}#初始化用户
        self.main_room=ChatRoom(self)#定义聊天室

    def handle_accept(self):
        conn,addr = self.accept()
        #等待传入连接。 返回代表连接的新套接字以及客户端的地址。 对于IP套接字，地址信息是一对（主机地址，端口）
        ChatSession(self,conn)


class ChatSession(asynchat.async_chat):
    '''负责和客户端通信'''
    def __init__(self,server,sock):
        asynchat.async_chat.__init__(self)
        self.server = server
        self.set_terminator(b'\n')
        self.data=[]
        self.name =None
        self.enter(LoginRoom(server))

    def enter(self,room):
        #从当前房间移除然后加入指定房间
        try:
            cur = self.room
        except AttributeError:#对象没有这个属性
            pass
        else:
            cur.remoe(self)
        self.room = room
        room.add(self)

    def collect_incoming_data(self, data):
        #接收客户端数据
        self.data.append(data.decode('utf-8'))
    def found_terminator(self):
        #当客户端一条数据结束时的处理
        line = ''.join(self.data)
        self.data=[]
        try:#退出聊天室的处理
            self.room.handle(self,line.encode('utf-8'))
        except EndSession:
            self.handle_close()

    def handle_close(self):
        #当session关闭时将进入LogoutRoom
        asynchat.async_chat.handle_close(self)
        self.enter(LogoutRoom(self.server))

class CommandHandler:
    '''命令处理类'''
    def unknow(self,session,cmd):
        #响应未知命令
        #通过asynchat.async_chat.push 方法发送消息
        session.push(('Unknow command {} \n'.format(cmd)).encode('utf-8'))
    def handle(self,session,line):
        line = line.decode()
        #命令处理
        if not line.strip():
            return
        parts = line.split(' ',1)
        cmd = parts[0]
        try:
            line =parts[1].strip()
        except IndexError:
            line = ''
        #通过协议代码执行相应的方法
        method = getattr(self,'do_'+cmd,None)
        try:
            method(session,line)
        except TypeError:#对类型无效的操作
            self.unknow(session,cmd)
class Room(CommandHandler):
    '''包含多个用户的环境，负责基本命令的处理和广播'''
    def __init__(self,server):
        self.server = server
        self.sessions=[]
    def add(self,session):#一个用户进入房间
        self.sessions.append(session)
    def remove(self,session):#一个用户离开房间
        self.sessions.remove(session)
    def broadcast(self,line):
        #向所有的用户发送指定消息
        #使用 asynchat.asyn_chat.push 方法发送数据
        for session in self.sessions:
            session.push(line)
    def do_logout(self,session,line):
        raise EndSession

class LoginRoom(Room):
    '''处理登录用户'''
    def add(self,session):
        #用户链接成功的回应
        Room.add(self,session)
        # 使用 asynchat.asyn_chat.push 方法发送数据
        session.push(b'Connect Success')

    def do_login(self,session,line):
        #用户登录逻辑
        name = line.strip()
        #获取用户名称
        if not name:
            session.push(b'UserName Empty')
        #检查是否有同名用户
        elif name in self.server.users:
            session.push(b'UserName Exist')
        #用户名检查成功后进入聊天室
        else:
            session.name=name
            session.enter(self.server.main_room)

class LogoutRoom(Room):
    '''处理退出用户'''
    def add(self,session):
        #从服务器中移除
        try:
            del self.server.users[session.name]
        except KeyError:#映射中没有这个键
            pass

class ChatRoom(Room):
    '''聊天的房间'''
    def add(self,session):
        #广播新用户进入
        session.push(b'Login Success')
        self.broadcast((session.name + 'has entered the room.\n').encode('utf-8'))
        self.server.users[session.name] = session
    def remove(self,session):
        '''广播用户离开'''
        Room.remove(self,session)
        self.broadcast((session.name + 'has left the room.\n').encode('utf-8'))
    def do_say(self,session,line):
        '''客户发送消息'''
        self.broadcast((session.name + ':' + line + '\n').encode('utf-8'))
    def do_look(self,session,line):
        '''查看在线用户'''
        session.push(b'OnlineUser:\n')
        for other in self.sessions:
            session.push((other.name + '\n').encode("utf-8"))

if __name__ == '__main__':

    s = ChatServer(PORT)
    try:
        print("chat server run at '0.0.0.0:{0}'".format(PORT))
        asyncore.loop()
    except KeyboardInterrupt:#用户中断执行(通常是输入^C)
        print('chat server exist')









