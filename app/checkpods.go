package app

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

type ResponseResultUserInfo struct {
	Status int         `json:"status"`
	Result interface{} `json:"result"`
	Msg    string      `json:"msg"`
}

func CheckPods(token, podsid string) (bool, error) {
	url := "https://sshpods.boxlinker.com/api/v1.0/sshpods/podsid/" + podsid

	client := &http.Client{}
	var b []byte
	req, err := http.NewRequest("GET", url, bytes.NewBuffer(b))
	if err != nil {
		return false, err
	}

	req.Header.Set("token", token)
	resp, err := client.Do(req)

	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return false, err
	}

	userinfo := ResponseResultUserInfo{}
	ret := json.Unmarshal(body, &userinfo)
	if ret != nil {
		fmt.Printf("token is error reason : %s \n", err.Error())
		return false, err
	}

	if userinfo.Status != 0 {
		fmt.Printf("token is userinfo.Status != 0 \n")
		return false, err
	}
	return true, nil
}
