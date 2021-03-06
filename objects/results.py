class Result:
    def __init__(self, outp_dir):
        self.result_dict = {
            'offender': {
                'touchdown': 0
            },
            'defender': {
                'passing failure': 0,
                'receiving failure': 0,
                'holder tackled': 0,
                'holder out': 0
            }
        }
        self.turns = 0
        self.outp_dir = outp_dir
    
    def record(self, winner, cause):
        self.result_dict[winner][cause] += 1
        self.turns += 1

    def summary(self):
        def_wins = sum(self.result_dict['defender'].values())
        msg = f"In a total of {self.turns} games:\n" + \
              f"\tOffender wins: {self.result_dict['offender']['touchdown']}\n" + \
              f"\t\ttouchdown: {self.result_dict['offender']['touchdown']}\n" + \
              f"\tDefender wins: {def_wins}\n" + \
              f"\t\tpassing failure: {self.result_dict['defender']['passing failure']}\n" +\
              f"\t\treceiving failure: {self.result_dict['defender']['receiving failure']}\n" +\
              f"\t\tholder tackled: {self.result_dict['defender']['holder tackled']}\n" +\
              f"\t\tholder out: {self.result_dict['defender']['holder out']}"
        
        print(msg)

        f = open(self.outp_dir, 'w')
        f.write(msg)
        f.close()

