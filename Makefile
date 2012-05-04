WEBMIN_FW_TCP_INCOMING = 22 80 443 8080 12320 12321

COMMON_CONF = postfix-local tkl-webcp appengine-docs
COMMON_OVERLAYS = tkl-webcp appengine

include $(FAB_PATH)/common/mk/turnkey.mk
