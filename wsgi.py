#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import uvicorn as uvicorn
from ibook import app

if __name__ == "__main__":
   uvicorn.run("ibook:app", host="localhost", port=8010, reload=True)
