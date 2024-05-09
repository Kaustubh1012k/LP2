def first_come_first_serve(tasks):
    schedule = []
    current_time = 0
    total_completion_time = 0

    for job_number, processing_time in tasks:
        start_time = max(current_time, job_number)  # Start time is either current time or job arrival time
        completion_time = start_time + processing_time  # Completion time
        total_completion_time += completion_time
        schedule.append((job_number, start_time, completion_time))

        current_time = completion_time  # Update current time

    return schedule, total_completion_time

# Get user input for job details
def get_job_details():
    tasks = []
    n = int(input("Enter the number of jobs: "))
    for i in range(1, n + 1):
        processing_time = int(input(f"Enter processing time for Job {i}: "))
        tasks.append((i, processing_time))
    return tasks

# Example usage:
tasks = get_job_details()
schedule, total_completion_time = first_come_first_serve(tasks)

print("Job Schedule:")
for task in schedule:
    job_number, start_time, completion_time = task
    print(f"Job {job_number}: Start Time={start_time}, Completion Time={completion_time}")

print(f"Total Completion Time: {total_completion_time}")
