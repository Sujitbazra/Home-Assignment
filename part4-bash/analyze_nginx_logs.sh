#!/bin/bash
      LOG_FILE=$1
      if [ ! -f "$LOG_FILE" ]; then
        echo "Log file not found"
        exit 1
      fi
      echo "Nginx Log Analysis"
      TOTAL=$(wc -l < $LOG_FILE)
      echo "Total Requests: $TOTAL"
      echo "Top 10 IPs:"
      awk '{print $1}' $LOG_FILE | sort | uniq -c | sort -nr | head -10
      echo "Top Endpoints:"
      awk '{print $7}' $LOG_FILE | sort | uniq -c | sort -nr | head -10
      echo "Errors:"
      awk '{print $9}' $LOG_FILE | grep -E '4[0-9]{2}' | wc -l
      awk '{print $9}' $LOG_FILE | grep -E '5[0-9]{2}' | wc -l