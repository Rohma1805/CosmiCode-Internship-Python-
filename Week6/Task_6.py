#Task_6:
import asyncio
import random

#Simulate an asynchronous I/O task
async def fetch_data(source):
    print(f"Fetching data from {source}...")
    await asyncio.sleep(random.randint(1, 3)) 
    print(f"Finished fetching from {source}")
    return f"Data from {source}"

#Main async function
async def main():
    sources = ["Database", "API", "File System", "Cache"]
    #Schedule tasks concurrently
    tasks = [fetch_data(source) for source in sources]
    #Run them concurrently and gather results
    results = await asyncio.gather(*tasks)
    print("\nAll data fetched successfully:")
    for r in results:
        print(r)
#Run the asyncio program
if __name__ == "__main__":
    asyncio.run(main())
