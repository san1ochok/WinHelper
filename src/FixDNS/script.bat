@echo off
title Fix DNS - Telegram: @alexndrev
ipconfig /flushdns
ipconfig /registerdns
ipconfig /renew
ipconfig /release