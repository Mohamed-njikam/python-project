from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

week_days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday",
             5: "Saturday", 6: "Sunday"}
today_date = datetime.today()
week_day = today_date.weekday()

engine = create_engine("sqlite:///todo.db?check_same_thread=False")

Base = declarative_base()


# table description
class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    task = Column(String, default="No task for today!")
    deadline = Column(Date, default=datetime.today())

    def __rep__(self):
        return self.task


# table creation in database
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

while True:
    # menu of the to-do list app
    print("1) Today's tasks", "2) Week's tasks", "3) All tasks",
          "4) Missed tasks", "5) Add task", "6) Delete task", "0) Exit", sep="\n")

    choice = input()

    # shows today's tasks
    if choice in ("1", "Today's tasks"):
        tasks = session.query(Task).filter(Task.deadline == today_date.date()).all()

        print(f"\nToday {today_date.day} {today_date.strftime('%b')}:")
        if len(tasks) == 0:
            print("Nothing to do!\n")
        else:
            for task_ in tasks:
                print(f"{task_.id}. {task_.task}\n")

    # shows the week's tasks
    elif choice in ("2", "Week's tasks"):
        for n in range(7):
            date_tracker = today_date + timedelta(days=n)
            task = session.query(Task).filter(Task.deadline == date_tracker.date()).all()

            print(f"{week_days.get(week_day + n, 'Monday')} {date_tracker.day} {today_date.strftime('%b')}:")
            if len(task) == 0:
                print("Nothing to do!")
                print()
            else:
                for task_ in task:
                    print(f"{task_.id}. {task_.task}")
                    print()

    # shows all the task with due dates
    elif choice in ("3", "All tasks"):
        all_tasks = session.query(Task).order_by(Task.deadline).all()

        print("All tasks:")
        if len(all_tasks) == 0:
            print("Nothing to do!")
        else:
            for task_ in all_tasks:
                print(f"{task_.id}. {task_.task}. {task_.deadline.day} {task_.deadline.strftime('%b')}")
        print()

    # shows missed tasks
    elif choice in ("4", "Missed tasks"):
        missed_tasks = session.query(Task).filter(Task.deadline < today_date.date()).order_by(Task.deadline).all()

        if len(missed_tasks) == 0:
            print("Nothing is missed!")
        else:
            for task_ in missed_tasks:
                print(f"{task_.id}. {task_.task}. {task_.deadline.day} {task_.deadline.strftime('%b')}")
        print()


    # adds a new task to the list
    elif choice in ("5", "Add task"):
        print("\nEnter task")
        n_task = input()
        print("Enter deadline")
        n_deadline = input()

        new_task = Task(task=n_task, deadline=datetime.strptime(n_deadline, "%Y-%m-%d"))
        session.add(new_task)
        session.commit()
        print("The task has been added!\n")

    elif choice in ("6", "Delete task"):
        tasks = session.query(Task).order_by(Task.deadline).all()

        for task_ in tasks:
            print(f"{task_.id}. {task_.task}. {task_.deadline.day} {task_.deadline.strftime('%b')}")

        print("Choose the number of the task you want to delete:")
        deleted_task = int(input())

        session.query(Task).filter(Task.id == deleted_task).delete()
        session.commit()
        print("The task has been deleted!")
        print()

    # exit the program
    elif choice in ("0", "Exit"):
        print("\nBye!")
        break
