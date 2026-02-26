## Authentication - Role Based Access Control (RBAC)
What they can do?


## Authorization - JWT token based access control (JSON Web Token) 
Proving who you are
Username + Password -> If correct, provides token -> instead of checking username and pwd everytime, we can send request using that token
JWT has 3 part:
1. Header - tells which algorithm is used (like HS256 - HS-Hexadecimal)
2. Payload - contains user info, role
3. Signature - used to verify the token
JWT workflow in FastAPI:
User -> Login -> FastAPI
                    |
                    v
         validates username and pwd 
                    |
                    v
        FastAPI generates JWT token
                    |
                    v
         User sends JWT in header 
                    |
                    v
          FastAPI validates token 
                    |
                    v
          Allow/deny the access