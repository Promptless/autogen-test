from magentic_one_helper import MagenticOneHelper
import asyncio
import json


async def main():
    # Create and initialize MagenticOne
    magnetic_one = MagenticOneHelper(logs_dir="./logs")
    await magnetic_one.initialize()
    print("MagenticOne initialized.")
    # Start a task and stream logs
    task = "code for fibonacci and run it"

    # Create task and log streaming tasks
    task_future = asyncio.create_task(magnetic_one.run_task(task))
    final_answer = None

    # Stream and process logs
    async for log_entry in magnetic_one.stream_logs():
        print(json.dumps(log_entry, indent=2))

    # Wait for task to complete
    await task_future

    # Get the final answer
    final_answer = magnetic_one.get_final_answer()

    if final_answer is not None:
        print(f"Final answer: {final_answer}")
    else:
        print("No final answer found in logs.")


if __name__ == "__main__":
    asyncio.run(main())