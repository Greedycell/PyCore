from Protocol.Messages.Client.Account.ClientHelloMessage import ClientHelloMessage
from Protocol.Messages.Client.Account.LoginMessage import LoginMessage
from Protocol.Messages.Client.Account.KeepAliveMessage import KeepAliveMessage

MessageFactory = {
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10108: KeepAliveMessage
}