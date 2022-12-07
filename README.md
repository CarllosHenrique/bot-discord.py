## My discord bot

The Saturday bot was created by me in order to add some animation to my Discord servers and to put my python skills to the test.

### built with

* [Python](https://www.python.org/)
* [Pip](https://pypi.org/project/pip/)
* [Discord.py](https://pypi.org/project/discord.py/)

### Diary

I've included an diary system in this bot, and I'll explain how it works >>>

There are three types of commands in the ```main.py``` file, from line 62 to line 96. (agenda, add, remove).
* Agenda - Showcase all of your saved annotations in one place. ```cogs/list.txt``` 
```ruby
   %agenda 
   ```
* Adicionar - This command creates notes in the diary. ```.txt``` together with the creator's ID_USER, which is added automatically.
```ruby
   %adicionar "text" 
   ```
* Remover - This command removes the line from your diary at the previous position; only a few inteiros are used.
```ruby
   %remover 5 
   ```

### Keep Alive

One way to keep your bot online indefinitely is to upload it to [Heroku](https://dashboard.heroku.com/) and use ```keep_alive.py```.

### installation

1. clone the repo
   ```sh
   git clone 
   ```
2. install dependencies
   ```sh
   python main.py
   ``` 
## contributing
1. fork the project
2. create your feature branch 
```sh
git checkout -b feature/AmazingFeature
```
3. commit your changes
```sh
git commit -m 'Add some AmazingFeature'
```
4. push to the branch 
```sh
git push origin feature/AmazingFeature
```
5. open a pull request
