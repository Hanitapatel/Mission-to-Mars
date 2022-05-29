{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "d79d4fcd",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, redirect, url_for\n",
    "from flask_pymongo import PyMongo\n",
    "import scraping"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "fe387527",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "93dbb33a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use flask_pymongo to set up mongo connection\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars_app\"\n",
    "mongo = PyMongo(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "75a5fcab",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define the route for the HTML page\n",
    "@app.route(\"/\")\n",
    "def index():\n",
    "   mars = mongo.db.mars.find_one()\n",
    "   return render_template(\"index.html\", mars=mars)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "04d55fbe",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define the route for the scrape new data using the code we've written.\n",
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "   mars = mongo.db.mars\n",
    "   mars_data = scraping.scrape_all()\n",
    "   mars.update_one({}, {\"$set\":mars_data}, upsert=True)\n",
    "   return redirect('/', code=302)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a866276b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__' (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)\n",
      "[2022-05-28 18:22:51,375] ERROR in app: Exception on / [GET]\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\Work\\anaconda3\\envs\\Python37Data\\lib\\site-packages\\flask\\app.py\", line 2077, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\Users\\Work\\anaconda3\\envs\\Python37Data\\lib\\site-packages\\flask\\app.py\", line 1525, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\Users\\Work\\anaconda3\\envs\\Python37Data\\lib\\site-packages\\flask\\app.py\", line 1523, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\Users\\Work\\anaconda3\\envs\\Python37Data\\lib\\site-packages\\flask\\app.py\", line 1509, in dispatch_request\n",
      "    return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)\n",
      "  File \"C:\\Users\\Work\\AppData\\Local\\Temp\\ipykernel_18740\\1541266139.py\", line 5, in index\n",
      "    return render_template(\"index.html\", mars=mars)\n",
      "  File \"C:\\Users\\Work\\anaconda3\\envs\\Python37Data\\lib\\site-packages\\flask\\templating.py\", line 149, in render_template\n",
      "    ctx.app.jinja_env.get_or_select_template(template_name_or_list),\n",
      "  File \"C:\\Users\\Work\\anaconda3\\envs\\Python37Data\\lib\\site-packages\\jinja2\\environment.py\", line 1081, in get_or_select_template\n",
      "    return self.get_template(template_name_or_list, parent, globals)\n",
      "  File \"C:\\Users\\Work\\anaconda3\\envs\\Python37Data\\lib\\site-packages\\jinja2\\environment.py\", line 1010, in get_template\n",
      "    return self._load_template(name, globals)\n",
      "  File \"C:\\Users\\Work\\anaconda3\\envs\\Python37Data\\lib\\site-packages\\jinja2\\environment.py\", line 969, in _load_template\n",
      "    template = self.loader.load(self, name, self.make_globals(globals))\n",
      "  File \"C:\\Users\\Work\\anaconda3\\envs\\Python37Data\\lib\\site-packages\\jinja2\\loaders.py\", line 126, in load\n",
      "    source, filename, uptodate = self.get_source(environment, name)\n",
      "  File \"C:\\Users\\Work\\anaconda3\\envs\\Python37Data\\lib\\site-packages\\flask\\templating.py\", line 59, in get_source\n",
      "    return self._get_source_fast(environment, template)\n",
      "  File \"C:\\Users\\Work\\anaconda3\\envs\\Python37Data\\lib\\site-packages\\flask\\templating.py\", line 95, in _get_source_fast\n",
      "    raise TemplateNotFound(template)\n",
      "jinja2.exceptions.TemplateNotFound: index.html\n",
      "127.0.0.1 - - [28/May/2022 18:22:51] \"GET / HTTP/1.1\" 500 -\n",
      "127.0.0.1 - - [28/May/2022 18:22:51] \"GET /favicon.ico HTTP/1.1\" 404 -\n",
      "[2022-05-28 18:25:02,454] ERROR in app: Exception on /scrape [GET]\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\Work\\anaconda3\\envs\\Python37Data\\lib\\site-packages\\flask\\app.py\", line 2077, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\Users\\Work\\anaconda3\\envs\\Python37Data\\lib\\site-packages\\flask\\app.py\", line 1525, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\Users\\Work\\anaconda3\\envs\\Python37Data\\lib\\site-packages\\flask\\app.py\", line 1523, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\Users\\Work\\anaconda3\\envs\\Python37Data\\lib\\site-packages\\flask\\app.py\", line 1509, in dispatch_request\n",
      "    return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)\n",
      "  File \"C:\\Users\\Work\\AppData\\Local\\Temp\\ipykernel_18740\\2289543216.py\", line 5, in scrape\n",
      "    mars_data = scraping.scrape_all()\n",
      "AttributeError: module 'scraping' has no attribute 'scrape_all'\n",
      "127.0.0.1 - - [28/May/2022 18:25:02] \"GET /scrape HTTP/1.1\" 500 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "   app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7fa033cb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
