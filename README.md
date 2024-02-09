# yao-benchmark
Yet another one benchmark (that nobody asked for)
### Long story short
<details>
<summary>Results table</summary>

| Framework   | Runtime | Server   | W[^1] | RPM[^2] | L[^3] | CPU[^4] | Mem[^4] |
|-------------|---------|----------|-------|---------|-------|---------|---------|
| Flask-RESTX | py38    | Gunicorn | 1     | xxx     | xx    | 30%     | 10%     |
</details>

[Google spreadsheet](https://docs.google.com/spreadsheets/d/1Cojv3-i-Jp5OBe26qyfy-kO59fkgCiZMujKfK0i-G1U/edit?usp=sharing)

*All the boring details can be found below.*

[^1]: Number of workers

[^2]: Requests per minute measured by Locust

[^3]: Number of lines of code excluding initial bootstrap (like `startproject` in Django)

[^4]: CPU and Memory consumption measured by `htop` tool during the test

### Server
#### Hardware
```
Dell Inspirion 3511 / Core i3-1115G4 / 32GB / SSD
```
#### Tools
```
pyenv 2.3.35
nvm 0.39.7
```
#### Runtimes
```
Python:
- 3.8.18
- 3.10.13
- 3.12.1
Pypy 3.10-7.3.15
Mojo 0.7.0
NodeJS:
- 16.20.2
- 18.19.0
- 20.11.0
Deno 1.40.3
Bun 1.0.26
```
#### Python servers
```
Gunicorn 21.2.0
Uvicorn 0.27.0.post1
Hypercorn 0.16.0
```
#### Python frameworks
```
Flask 3.0.2
Django 5.0.2
Starlette 0.36.3
```
#### Python REST-API
```
Flask-RESTX 1.3.0
Django REST framework 3.14.0
Django Ninja 1.1.0
FastAPI 0.109.2
Blacksheep 2.0.6
```
#### NodeJS frameworks
```
Express 4.18.2
Koa 2.15.0
Fastify 4.26.0
Deno 1.40.30
Elysia 1.0.50
```
### Mojo framework
```
Lightbug 0.1.1-alpha
```
### Testing environment
```
Dell Latitude 5440 / Core i7-1365U / 32GB / SSD
Python 3.10.12
Locust 2.22.0 (Master + 3 Workers, 10k users)
```
### Network
```
TP-Link TL-WR940N
```
### Testing scenario
```
Request: POST /api/
{
  "payload": "<GUID4>"
}

Response: 200 OK
{
  "result": "<SHA3_512(payload)>"
}
```
### Conclusion
I really appreciate you've got this long. No conclusions, the numbers talks by itselves.
