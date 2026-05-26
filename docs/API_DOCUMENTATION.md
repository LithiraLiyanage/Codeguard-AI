# API Documentation

## Auth

`POST /api/auth/register`
```json
{"name":"Lithira","email":"lithira@example.com","password":"password123","confirmPassword":"password123"}
```

`POST /api/auth/login`
```json
{"email":"lithira@example.com","password":"password123"}
```

## Reviews

`POST /api/reviews/analyze-code`
```json
{"projectName":"Demo","fileName":"app.js","language":"javascript","code":"console.log('hello')"}
```

`POST /api/reviews/analyze-file` uses FormData: `codeFile`, `language`, `projectName`.

`POST /api/reviews/analyze-github`
```json
{"githubUrl":"https://github.com/user/repo","projectName":"Repo Review"}
```
