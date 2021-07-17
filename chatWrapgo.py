type Chatbot struct {
	Message string                 `json:"message"`
}

func chatbot(MESSAGE, BOTNAME, OWNERNAME, USERID string) (*Chatbot, error) {
	resp, err := http.Get(fmt.Sprintf("https://api.affiliateplus.xyz/api/chatbot?message=%v&botname=%v&ownername=%v&user=%v", MESSAGE, BOTNAME, OWNERNAME, USERID))
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()
	var chat = new(Response)
	json.NewDecoder(resp.Body).Decode(&chat)
	return &chat.Data.Chatbot, nil
}
