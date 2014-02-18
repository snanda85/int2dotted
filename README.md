int2dotted
==========

A lightweight tool to convert IP addresses formats between Integer &amp; Expanded forms

Usage
-----

    python int2dotted.py <Integer Or IP>

If an integer is passed, it will be converted to expanded form
If an IP is passed, it will be converted to integer

Examples
--------

    # IPv4
    ./int2dotted.py 10.10.2.3
    168428035

    ./int2dotted.py 168428035
    10.10.2.3

    # IPv6
    ./int2dotted.py 2001:0db8:85a3:0000:0000:8a2e:0370:7334
    42540766452641154071740215577757643572

    ./int2dotted.py 42540766452641154071740215577757643572
    2001:db8:85a3::8a2e:370:7334

