let color = '#3aa757';

chrome.runtime.onInstalled.addListener(() => {
  console.log('%cRunning...', `color: ${color}`);
});
