export default {
  clear() {
    localStorage.removeItem('playerName');
    localStorage.removeItem('participationScore');
  },
  savePlayerName(playerName) {
    window.localStorage.setItem('playerName', playerName);
  },
  getPlayerName() {
    return window.localStorage.getItem('playerName');
  },
  saveParticipationScore(participationScore) {
    window.localStorage.setItem('participationScore', JSON.stringify(participationScore));
  },
  getParticipationScore() {
    const stored = window.localStorage.getItem('participationScore');
    return stored ? JSON.parse(stored) : null;
  },
};
