class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_

        self.name = name

        self.company = company

        self.workers = []

    @property
    def worker(self):
        return self.workers

    @worker.setter
    def worker(self, worker):
        if worker.boss == self.name and worker.company == self.company:
            self.workers.append(worker)


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_

        self.name = name

        self.company = company

        self.boss = boss


b = Boss(12344, 'Artem', 'PDF')
w = Worker(23456, 'Alena', 'PDF', b)

