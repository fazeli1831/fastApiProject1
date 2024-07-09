from typing import List
from fastapi import FastAPI, Path
import multiprocessing
import random
from multiprocessing import Pool

app = FastAPI()

# Function 1
def function_square1(data):
    result = data * data
    return result

# Function 2
def function_square2(data):
    result = data + data
    return result

# Function 3
def function_square3(data):
    result = data * random.randint(1, 10)
    return result

# Multiprocessing function
def run_multiprocessing_pool(function, inputs: List[int]):
    pool = Pool(processes=4)
    pool_outputs = pool.map(function, inputs)
    pool.close()
    pool.join()
    return pool_outputs

@app.get("/square1/{data}", response_model=List[int])
async def square_data1(data: int = Path(..., description="Input data to square")):
    inputs = list(range(data))
    return run_multiprocessing_pool(function_square1, inputs)

@app.get("/square2/{data}", response_model=List[int])
async def square_data2(data: int = Path(..., description="Input data to add")):
    inputs = list(range(data))
    return run_multiprocessing_pool(function_square2, inputs)

@app.get("/square3/{data}", response_model=List[int])
async def square_data3(data: int = Path(..., description="Input data to multiply randomly")):
    inputs = list(range(data))
    return run_multiprocessing_pool(function_square3, inputs)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
