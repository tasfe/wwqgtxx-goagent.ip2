def main():
    import httplib
    conn = httplib.HTTPConnection("www.g.com", 80, False)
    conn.request('get', '/', headers = {"Host": "www.google.com","User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5","Accept": "text/plain"})
    res = conn.getresponse()
    print 'version:', res.version
    print 'reason:', res.reason
    print 'status:', res.status
    print 'msg:', res.msg
    print 'headers:', res.getheaders()
    #html
    print '\n' + '-' * 50 + '\n'
    print res.read()
    conn.close()

if __name__ == '__main__':
    main()
