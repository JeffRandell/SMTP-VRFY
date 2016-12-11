# SMTP-VRFY
smtp-vrfy.py checks usernames against mail servers.

#### CLI bash loop for multiple servers
Try this.
```
# for result in `nmap -vv -oG - --open -Pn -p25 10.11.1.0/24 | grep -v Nmap | grep -v scanned | grep -v "Status" | cut -d" " -f 2`; do ./smtp-vrfy.py $result 25 temp-username-list; done
```

#### Update 2016-12-11
* I've split smtp-vrfy into two tools, the single-host tool and a multi-host tool, "smtp-vrfy-multi.py". Multi requires some work for stability.
* I've improved the output readability, although this tool is still geared more toward domain discovery than specific host account information.
