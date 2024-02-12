# yao-benchmark
Yet another one benchmark (that nobody asked for)
### Long story short
<details>
<summary>Results table</summary>
Best result for each framework powered by 1 worker.

| Framework   | Runtime | Server   | RPM [^1] | L [^2] | CPU% [^3] | Mem% [^3] |
|-------------|---------|----------|----------|--------|-----------|-----------|
| Flask-RESTX | py310   | Gunicorn | xxx      | xx     | 30        | 10        |
</details>

The full data set is presented in this [google spreadsheet](https://docs.google.com/spreadsheets/d/1Cojv3-i-Jp5OBe26qyfy-kO59fkgCiZMujKfK0i-G1U/edit?usp=sharing).

*All the boring details can be found below.*

[^1]: Requests per minute measured by Locust

[^2]: Number of lines of code excluding initial bootstrap (like `startproject` in Django)

[^3]: CPU and Memory consumption measured by `htop` tool during the test

### Server
- Dell Inspiron 3511 / Core i3-1115G4 / 32GB / SSD
- xUbuntu 22.04.3 LTS
#### Tools
```
pyenv 2.3.35
nvm 0.39.7
```
#### Runtimes
```
Python:
- 3.10.13
- 3.12.1
Pypy 3.10-7.3.15
Mojo 0.7.0
NodeJS:
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
#### JS/TS frameworks
```
Express 4.18.2
Koa 2.15.0
Fastify 4.26.0
Deno 1.40.30
Elysia 1.0.50
```
#### Mojo framework
```
Lightbug 0.1.1-alpha
```
### Testing environment
```
Dell Latitude 5440 / Core i7-1365U / 32GB / SSD
Ubuntu 22.04.3 LTS
Python 3.10.12
Locust 2.22.0 (10 Workers, 100 users)
```
### Network
```
TP-Link TL-WR940N
```
### Testing scenario
```
Request: POST /api/
{
  "payload": "<UUID4>"
}

Response: 200 OK
{
  "result": "<SHA3_512(payload)>"
}
```
### Locust configuration
```
$ cd locust && locust --master
$ cd locust && locust --worker  # 10 times
```
### Conclusion
I really appreciate you've got this long. No conclusions, the numbers speaks for itself.
