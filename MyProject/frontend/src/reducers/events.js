import { GET_EVENTS } from '../actions/types.js';

const initialState = {
    events: []
}

export default function(state = initialState, action) {
    switch(action.type) {
        case GET_EVENTS:
            return {
                ...state,
                events: action.payload
            }
        default:
            return state;
    }
}