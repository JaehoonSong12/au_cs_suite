// src/utils/RefreshManager.js
class RefreshManager {
    constructor() {
        this.refreshHandlers = new Set();
    }

    register(handler) {
        this.refreshHandlers.add(handler);
    }

    unregister(handler) {
        this.refreshHandlers.delete(handler);
    }

    triggerRefresh() {
        this.refreshHandlers.forEach((handler) => handler());
    }
}
  
const refreshManager = new RefreshManager();
export default refreshManager;