from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl = 'auth/token')

class Hash():
    def bcrypt(password:str):
        return pwd_cxt.hash(password)
    
    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)