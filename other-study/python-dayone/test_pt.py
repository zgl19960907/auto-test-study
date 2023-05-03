import openpyxl
import pytest
from excel_deal import ex_read
from deal_data import deal_tq
'''
pytest使用规则，
1、文件名必须是test_开头或者_test结尾
2、类名必须是大写的Test
'''
class TestCase:
    # 一个test代表一个用例
    # pytest 参数化
    @pytest.mark.parametrize('case', ex_read())
    def test_01(self, case):
        # print(case)
        id = case[0]
        url = case[1]
        data = case[2]
        method = case[3]
        expect = case[4]  # 实际结果
        res = deal_tq(url, data, method)
        # print(res.json())
        # 判断预期结果和实际结果是否一致res.json()['cityid']
        # 注意数据类型转换
        try:
            assert str(expect) == res.json()['cityid']
            remsg = '用例成功'
        except Exception as e:
            remsg = '用例失败'
        webhook = openpyxl.load_workbook('case.xlsx')
        sheet = webhook['Sheet1']
        sheet.cell(id+1, 6).value = remsg
        webhook.save('case.xlsx')


if __name__ == '__main__':
    pytest.main(['-sv'])