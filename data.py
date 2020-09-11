import json
import os

class Data:

    def __init__(self, path:str=None):
        self.__path = path

        if path:
            print("初次运行初始化")
            self.__read_1()
            self.__analysis()
            self.__save2json()
        else:
            self.__read_2()


    def __read_1(self):
        self.__dicts = []
        with open(self.__path, 'r', encoding='utf-8') as f:
            self.__jsons = [x for x in f.read().split('\n') if len(x)>0]
            for self.__json in self.__jsons:
                self.__dicts.append(json.loads(self.__json))


    def __analysis(self):
        self.__types = ['PushEvent', 'IssueCommentEvent', 'IssuesEvent', 'PullRequestEvent']
        self.__cnt_perP = {}
        self.__cnt_perR = {}
        self.__cnt_perPperR = {}

        for self.__dict in self.__dicts:
            # 如果属于四种事件之一 则增加相应值
            if self.__dict['type'] in self.__types:
                self.__event = self.__dict['type']
                self.__name = self.__dict['actor']['login']
                self.__repo = self.__dict['repo']['name']
                self.__cnt_perP[self.__name + self.__event] = self.__cnt_perP.get(self.__name + self.__event, 0) + 1
                self.__cnt_perR[self.__repo + self.__event] = self.__cnt_perP.get(self.__repo + self.__event, 0) + 1
                self.__cnt_perPperR[self.__name + self.__repo + self.__event] = self.__cnt_perPperR.get(self.__name + self.__repo + self.__event, 0) + 1


    def __save2json(self):
        with open("1.json", 'w', encoding='utf-8') as f:
            json.dump(self.__cnt_perP, f)
        with open("2.json", 'w', encoding='utf-8') as f:
            json.dump(self.__cnt_perR, f)
        with open("3.json", 'w', encoding='utf-8') as f:
            json.dump(self.__cnt_perPperR, f)
        print("Save to json files successfully!")


    def __read_2(self):
        self.__cnt_perP = {}
        self.__cnt_perR = {}
        self.__cnt_perPperR = {}
        with open("1.json", encoding='utf-8') as f:
            self.__cnt_perP = json.load(f)
        with open("2.json", encoding='utf-8') as f:
            self.__cnt_perR = json.load(f)
        with open("1.json", encoding='utf-8') as f:
            self.__cnt_perPperR = json.load(f)


    # get value from dictionary

    def get_cnt_user(self, user:str, event:str) -> int:
        return self.__cnt_perP.get(user + event, 0)

    def get_cnt_repo(self, repo:str, event:str) -> int:
        return self.__cnt_perR.get(repo + event, 0)

    def get_cnt_user_and_repo(self, user, repo, event) -> int:
        return self.__cnt_perPperR.get(user + repo + event, 0)