import yaml
from config import config_path

def get_true_value(di1,u):
    """
    递归函数
    :param di1: yaml配置文件
    :param u: 拆分后的查询内容（list）
    :return: 最终值
    """
    m = di1.get(u[0])
    u.remove(u[0])
    if type(m) == dict:
        if u !=[]:
          return get_true_value(m,u)

    return m


class ReadYaml:
    """
    读取yaml文件字段内容
    默认读取文件init.yamlaaw
    """

    def get_yaml(self,yaml_file):
        """
        读取yaml文件
        :return: 字典
        """
        with open(config_path.cf + '/' +yaml_file, 'r', encoding='utf-8') as f:
            file = yaml.load(f, Loader=yaml.FullLoader)
        f.close()

        return file

    def get_value(self,yaml_file, name):
        """
        读取任意节点字段值
        :param name: 查询内容，如：db.host
        :return: 字段值
        """
        if '.' not in name:
            return self.get_yaml(yaml_file=yaml_file).get(name)
        else:
            di1 = self.get_yaml(yaml_file=yaml_file)
            u = name.split('.')
            return get_true_value(di1,u)





