$ORIGIN example.com.
@	3600 IN	SOA sns.example.com. example.com (
				2018070532 ; serial
				7200       ; refresh in seconds (2 hours is 7200)
				3600       ; retry (1 hour)
				1209600    ; expire (2 weeks)
				3600       ; minimum (1 hour)
				)

	3600 IN NS ns1.example.com.
	3600 IN NS ns2.example.com.

example.com		IN A     127.0.0.1
ns1			IN A     127.0.0.1
ns2			IN A     172.16.12.1
rtr			IN A     172.16.12.1
;############# - Raspberry PI svc - ##############
TopHat			IN A     172.16.12.18;
traefik         	IN A     172.16.12.18;
example.com.    	IN A     172.16.12.18;
*.traefik.example.com.  IN A     172.16.12.18;

; NOTES:
; If you wish for this file to be reloaded after change,
; Make sure to increment the serial number !
