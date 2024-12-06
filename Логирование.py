
import logging
import unittest
from rt_with_exceptions import Runner


logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log",
                    encoding="utf-8", format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner1 = Runner("Ivan")
            for i in range(10):
                runner1.walk()
            self.assertEqual(runner1.distance, 50)
            logging.info("'test_walk' выполнен успешно")
        except ValueError as exc:
            logging.warning("Неверная скорость для Runner", exc_info = exc)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner2 = Runner("Petr")
            for i in range(10):
                runner2.run()
            self.assertEqual(runner2.distance, 100)
            logging.info("'test_run' выполнен успешно")
        except ValueError as exc:
            logging.warning("Неверный тип данных для обьекта Runner", exc_info = exc)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner("Ivan")
        runner2 = Runner("Petr")
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertEqual(runner1.distance != runner2.distance, True)





if __name__ == "__main__":
    unittest.main()


