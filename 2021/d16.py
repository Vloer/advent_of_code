from __future__ import annotations
from pathlib import Path
from time import perf_counter

input_file = Path(__file__).parent / "inputs" / "d16.txt"


def parse_input(txt_file: str = input_file) -> list[int]:
    with open(txt_file, 'r') as f:
        return(f.read())
        

inp = parse_input()
test = ['D2FE28', '38006F45291200', 'EE00D40C823060', '8A004A801A8002F478',
        '620080001611562C8802118E34', 'C0015000016115A2E0802F182340', 'A0016C880162017C3686B18A3D4780']
test2 = ['C200B40A82', '04005AC33890', '880086C3E88112', 'CE00C43D881120', 'D8005AC2A8F0', 'F600BC2D8F', '9C005AC2F8F0', '9C0141080250320F1802104A08']


def hex_to_bin(s: str) -> bin:
    return bin(int(s, 16))[2:].zfill(len(s)*4)


def cut(b: str, start: int, end: int) -> str | str:
    new = b[start:end]
    remaining = b[end:]
    return remaining, new


def _int(b: str) -> int:
    return int(b, 2)


def get_total_versions(p: Packet) -> int:
    child_sum = 0
    for child in p.children:
        child_sum += get_total_versions(child)
    return p.version + child_sum 



class Packet:
    def __init__(self, binary: str, parent: Packet = None, printing=False):
        global GLOBAL_PACKET_COUNT
        global PRINT_SETTING
        GLOBAL_PACKET_COUNT += 1
        self.parent: Packet = parent
        self.children: list[Packet] = []
        self.binary: str = binary
        self.binary_remaining: str = ''
        self.version: int = None
        self.type_id: int = None
        self.operator: int = None
        self.literal_value: int = None
        self.total_length: int = None
        self.num_subpackets: int = None
        self.get_version_typeid()
        if self.type_id == 4:
            self.get_literal()
            if PRINT_SETTING:
                print(f'Packet {GLOBAL_PACKET_COUNT}\n\tversion: {self.version}\n\tliteral: {self.literal_value}')
        else:
            self.get_operator()
            if PRINT_SETTING:
                if self.operator == 0:
                    print(f'Packet {GLOBAL_PACKET_COUNT}\n\tversion: {self.version}\n\toperator: {self.operator}\n\tlength: {self.total_length}')
                else:
                    print(f'Packet {GLOBAL_PACKET_COUNT}\n\tversion: {self.version}\n\toperator: {self.operator}\n\tsubpackets: {self.num_subpackets}')
            self.analyze_subpackets()

    def get_version_typeid(self):
        self.binary, v = cut(self.binary, 0, 3)
        self.binary, t = cut(self.binary, 0, 3)
        self.version = _int(v)
        self.type_id = _int(t)

    def get_literal(self):
        new_str = ''
        while True:
            self.binary, s = cut(self.binary, 0, 5)
            new_str += s[1:]
            if s.startswith('0') or len(self.binary) < 6:
                self.literal_value = _int(new_str)
                break

    def get_operator(self):
        self.binary, lti = cut(self.binary, 0, 1)
        self.operator = int(lti)
        if self.operator == 0:
            self.binary, tl = cut(self.binary, 0, 15)
            self.total_length = _int(tl)
        elif self.operator == 1:
            self.binary, nsp = cut(self.binary, 0, 11)
            self.num_subpackets = _int(nsp)

    def analyze_subpackets(self):
        if self.operator == 0:
            self.binary_remaining, self.binary = cut(self.binary, 0, self.total_length)
            while len(self.binary) > 6:
                subpacket = Packet(self.binary, parent=self)
                self.children.append(subpacket)
                self.binary = subpacket.binary
            self.binary = self.binary_remaining
        elif self.operator == 1:
            current_subpacket = 0
            for _ in range(self.num_subpackets):
                current_subpacket += 1
                subpacket = Packet(self.binary, parent=self)
                self.children.append(subpacket)
                self.binary = subpacket.binary


def solve(data: str, result: int = 0, part1=True) -> int:
    global GLOBAL_PACKET_COUNT
    global PRINT_SETTING
    GLOBAL_PACKET_COUNT = 0
    PRINT_SETTING = False
    if part1:
        if isinstance(data, list):
            for code in data:
                GLOBAL_PACKET_COUNT = 0
                print(f'\nStarting input \'{code}\'')
                binary = hex_to_bin(code)
                outer_packet = Packet(binary)
                result = get_total_versions(outer_packet)
                print(result)
        else:
            print(f'\nStarting input \'{data}\'')
            binary = hex_to_bin(data)
            outer_packet = Packet(binary)
            result = get_total_versions(outer_packet)
    return result


timing_1 = perf_counter()
answer_1 = solve(test, part1=True)
print(f"Answer 1 took {perf_counter()-timing_1}: {answer_1}")
timing_2 = perf_counter()
answer_2 = solve(test, part1=False)
print(f"Answer 2 took {perf_counter()-timing_2}: {answer_2}")
